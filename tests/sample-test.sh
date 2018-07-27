# This doesn't actually do anything
# Assuming that the TMM *.c code is in the ttmm/alphaz_stuff/out directory, we would want this script to do something like the following:
# - execute make in the ttmm/alphaz_stuff/out directory to try to compile the code. If it doesn't compile, then report failed and quit
# - after it compiles, actually do a few matrix multiplications, and write the output to some file
# - look at the answer in that file and 'consult the oracle', to figure out if the answer matches what we expect.  If it doesn't then report failure and quit
#
# To exit with an error in a shell script, we can use the line:
#   exit 1 # terminate and indicate error
#
# So as an example, assuming we have a file with the input values of a matrix, a sample test (psuedo code) might look like this:
#   cat input_values | ./ttmm/alphaz_stuff/out/TTMM.check 5000 > output_values
#   if (output_values.contents != correct_values.contents)
#       exit 1
#   
# we could either put all of this into one big test script OR individual scripts and define individual steps in the jenkins file

echo 'I did nothing'

