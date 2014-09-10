requirejs.config({
    paths: {
        livescript: "lib/livescript",
        ls: "lib/ls",
        prelude: "lib/prelude-browser",
        jquery: "lib/zepto",
        mustache: "lib/mustache",
        backbone: "lib/backbone",
　      underscore: "lib/lodash"
    },
    shim: {
        livescript: {
            exports: "LiveScript"
        },
        prelude: {
            deps: ["livescript"],
            exports: "prelude"
        },
        ls: {
            deps: ["livescript"]
        },
        backbone: {
            deps: ["jquery", "underscore"],
            exports: "Backbone"
        },
        mustache: {
            exports: "mustache"
        },
        underscore: {
            exports: "_"
        },
        jquery: {
            exports: "$"
        }
    }
});

requirejs(["ls!main"], function () {

});

