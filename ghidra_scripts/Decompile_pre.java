import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.util.*;
import ghidra.program.model.reloc.*;
import ghidra.program.model.data.*;
import ghidra.program.model.block.*;
import ghidra.program.model.symbol.*;
import ghidra.program.model.scalar.*;
import ghidra.program.model.mem.*;
import ghidra.program.model.listing.*;
import ghidra.program.model.lang.*;
import ghidra.program.model.pcode.*;
import ghidra.program.model.address.*;
import ghidra.app.script.GatherParamPanel;
import ghidra.app.script.GhidraScript;
import ghidra.app.util.Option;
import ghidra.app.util.OptionException;
import ghidra.app.util.exporter.CppExporter;
import ghidra.app.util.exporter.ExporterException;

public class Decompile_pre extends GhidraScript{
    private static Logger log;

    public Decompile_pre() {
        log = LogManager.getLogger(Decompile_pre.class);
    }

    @Override
    public void run() throws Exception {
        //muqi change start
setAnalysisOption(currentProgram, "Decompiler Parameter ID", "true");
setAnalysisOption(currentProgram, "Apply Data Archives", "true");
setAnalysisOption(currentProgram, "x86 Constant Reference Analyzer", "true");
setAnalysisOption(currentProgram, "DWARF", "false");
        //muqi change end
    }

    
}
