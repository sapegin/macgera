module.exports = function(grunt) {

    grunt.initConfig({

        stylus: {
            compile: {
                files: {
                    'css/style.css' : 'styl/style.styl'
                }
            }
        },

        watch: {
            options: {
                livereload: true,
            },
            stylus: {
                files: 'styl/**',
                tasks: 'stylus'
            },
        },

        connect: {
            server: {
                post: 8000, 
                base: './'
            }
        }

    });

    grunt.loadNpmTasks('grunt-contrib-connect');
    grunt.loadNpmTasks('grunt-contrib-stylus');
    grunt.loadNpmTasks('grunt-contrib-watch');


    grunt.registerTask('run', ['connect', 'stylus', 'watch']);
    grunt.registerTask('default', ['run'])

};