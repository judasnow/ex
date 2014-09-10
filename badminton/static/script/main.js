requirejs.config({
    paths: {
        livescript: "lib/livescript",
        ls: "lib/ls"
        //prelude: "lib/prelude-browser"
    },

    shim: {
        livescript: {
            exports: "LiveScript"
        },
        //prelude: {
        //    deps: ["livescript"],
        //    exports: "prelude"
        //},
        ls: {
            deps: ["livescript"]
        }
    }
});

requirejs(["ls!main"], function () {
    // Main
});


