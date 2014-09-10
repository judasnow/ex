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
        }
    });

    //grunt.loadNpmTasks("grunt-ts");

    grunt.registerTask("default", []);
}


