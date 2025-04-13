// console.log("Script injected successfully");   Interceptor.replace(Module.findExportByName("kernel32.dll", "GetLastError"),    new NativeCallback(function() {     console.log("GetLastError called, returning 13811");     return 13811;    }, "uint32", []));
console.log("Script injected successfully");
Interceptor.replace(Module.findExportByName("kernel32.dll", "GetLastError"),
    new NativeCallback(function() { 
        console.log("GetLastError called, returning 13811");
        return 13811; 
    }, "uint32", []));
// Pause execution to allow you to inspect memory or attach with a debugger.
setTimeout(function(){ console.log("Pausing for inspection..."); }, 10000);
