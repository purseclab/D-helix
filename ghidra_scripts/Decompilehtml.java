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
//import ghidra.app.script.GatherParamPanel;
import ghidra.app.script.GhidraScript;
import ghidra.app.util.Option;
import ghidra.app.util.OptionException;
import ghidra.app.util.exporter.CppExporter;
import ghidra.app.util.exporter.HtmlExporter;
import ghidra.app.util.exporter.ExporterException;

public class Decompilehtml extends GhidraScript{
    private static Logger log;

    public Decompilehtml() {
        log = LogManager.getLogger(Decompilehtml.class);
    }

    public void export(String filename) {
        File outputFile = new File(filename);
         HtmlExporter htmlExporter = new  HtmlExporter();
         //HtmlExporter.setExporterServiceProvider(state.getTool());

		

        try {
            htmlExporter.export(outputFile, currentProgram, null, monitor);
        } catch (IOException e) {
            log.error("Failed writing decompiled code as output", e);
        } catch (ExporterException e) {
            log.error("Failed to export with cppExporter", e);
        }
    }

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        export(args[0]);
    }

    
}
