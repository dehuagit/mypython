
%module hellowrap

%{
#include <hellolib.h>
%}


/**or include hellolib.h and use _i arg/
** or %include "..//hello*/
extern char * message(char *);






