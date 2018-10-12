prog = ReadAlphabets("./TMM.ab");
system = "TMM";
outDir = "./out";

# generate codes
generateWriteCode(prog, system, options, outDir);
generateWrapper(prog, system, outDir);
generateMakefile(prog, system, outDir);
