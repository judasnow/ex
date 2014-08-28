module.exports = function (grunt) {
"use strict";

    // Project configuration.
    grunt.initConfig({
        //pkg: grunt.file.readJSON('package.json'),
        uglify: {
          options: {
            //banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
          },
          build: {
            //src: 'src/<%= pkg.name %>.js',
            //dest: 'build/<%= pkg.name %>.min.js'
          }
        },

        ts: {
            options: {
                target: "es5",
                //module: "",
                sourceMap: true,
                declaration: false,
                removeComments: true
            },

            build: {
                watch: "static/src/ts/",
                src: ["static/src/ts/*.ts"],
                outDir: "static/build/js/",
                out: "static/build/js/all.js",
            }
        }

    });

    grunt.loadNpmTasks("grunt-ts");

    grunt.registerTask("default", ["ts:build"]);
}


