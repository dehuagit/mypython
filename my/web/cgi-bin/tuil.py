
import sys
import os
#return a list of topen
def sortgenefile(countfile, writefile):
  backup = sys.stdout
  with open(countfile) as mfile, open(writefile,'w') as fout:
    res=[]
    header =  ','.join(mfile.readline().rstrip().split())
    sys.stdout = fout
    for line in  mfile.readlines():
      line = line.rstrip()
      res.append(tuple(line.split()))
    res.sort(key=lambda x:x[1])   # sort by the gene name
    print(header)
    for m in res:
      print(','.join(m))
  sys.stdout = backup

#################################################################
import sqlite3
class CommDB:
  def __init__(self, dbfile):
    self.dbfile = dbfile

  def connect(self):
    self.conn = sqlite3.connect(self.dbfile)
    self.curs = self.conn.cursor()

  def creattable(self, tbsql):
    self.curs.execute(tbsql)

  def insertdata(self, insertsql,  beinsertfile, filesplit="",
                 discardheader=True):
    with open(beinsertfile) as mfile:
      if discardheader:
        header = mfile.readline()
      for line in  mfile.readlines():
        if not filesplit:
          myrecord = line.rstrip().split()
        else:
          myrecord = line.rstrip().split(filesplit)
        self.curs.execute(insertsql, myrecord)
      self.conn.commit()

  def createindex(self, tablename, field):
    createindex = "create index index_%s on %s(%s)" %(tablename, tablename, field)
    self.curs.execute(createindex)

  def select(self, selectsql):
    self.curs.execute(selectsql)
    return self.curs.fetchall()

  def close(self):
    self.conn.close()


###############################################################

def rankselectsql():
  sql = """
  select totalDetailG.gene, totalDetailG.GroupNUM, GroupG.GroupTotal,
  DetailG.ConcatR1, DetailG.ConcatR2
  from 
  (select gene,  GROUP_CONCAT(R1, ";") AS ConcatR1, GROUP_CONCAT(R2, ";") AS
   ConcatR2 from magecko_count group by gene) AS DetailG
  ,
  (select gene, count(*) as GroupNum from magecko_count where (R1+R2) > 0 group
   by gene ) AS totalDetailG
  ,
  (select gene, count(*) as GroupTotal from magecko_count group by gene)  AS
  GroupG
  where DetailG.gene = totalDetailG.gene and DetailG.gene = GroupG.gene
  order by totalDetailG.GroupNUM DESC;

  """
  return sql


def generaterankfile(dbfile, countfile, mageckolib, writefile):
  if os.path.exists(dbfile):
    os.remove(dbfile)
  rankdb = CommDB(dbfile)
  rankdb.connect()
  rankdb.creattable('create table magecko_count(sgRNA TEXT NOT NULL, GENE TEXT NOT NULL, R1 INT NOT NULL, R2 INT NOT NULL)')
  rankdb.insertdata('insert into magecko_count values(?, ?, ?, ?)', countfile)
  rankdb.createindex('magecko_count', 'GENE')
  #rankdb.creattable('create table magecko_lib(sgRNA TEXT NOT NULL, SEQ TEXT NOT NULL, GENE INT NOT NULL)')
  #rankdb.insertdata('insert into magecko_lib values(?, ?, ?)', mageckolib, ",", False)
  #rankdb.createindex("magecko_lib", "sgRNA")
  with open(writefile, 'w') as rankfile:
    header = ["gene", "GroupNumLarge0","GroupTotal", "R1Concat", "R2Concat"]
    rankfile.write(','.join(header) + "\n")
    for row in rankdb.select(rankselectsql()):
      result = "%s,%s,%s,%s,%s\n" % (row)
      rankfile.write(result)
    rankdb.close()



if __name__ == '__main__':
  if False:
    sortgenefile("./test.gene","./test.gene.sort")
    print("hello in colose")
  else:
    print('Test sqlitedb')
    generaterankfile("./testdb", "./test.gene", "./testlib", "./test.rank")
