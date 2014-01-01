module.exports = function(grunt) {

    grunt.initConfig({

        stylus: {
            compile: {
                files: {
                    'css/style.css' : 'styl/style.styl'
                }
            }
        },

        autoprefixer: {
            options: {
                browsers: ['last 2 version']
            },
            multiple_files: {
                expand: true,
                flatten: true,
                src: 'css/style.css',
                dest: 'static/css/'
            }
        },

        imagemin: {
            dynamic: {
                files: [{
                    expand: true,
                    cwd: 'images/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: 'static/images/'
                }]
            }
        },

        watch: {
            options: {
                livereload: true,
            },
            stylus: {
                files: 'styl/**',
                tasks: ['stylus', 'autoprefixer']
            },
            autoprefixer: {
                files: 'css/**',
                tasks: ['autoprefixer']
            },
            images: {
                files: ['images/**/*.{png,jpg,gif}', 'images/*.{png,jpg,gif}'],
                tasks: ['imagemin'],
            }
        },

        connect: {
            server: {
                post: 8000,
                base: './'
            }
        }

    });

    require('load-grunt-tasks')(grunt);


    grunt.registerTask('run', ['connect', 'imagemin', 'stylus', 'autoprefixer', 'watch']);
    grunt.registerTask('default', ['run'])

};