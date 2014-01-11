module.exports = function(grunt) {

    grunt.initConfig({

        stylus: {
            compile: {
                files: {
                    'static/src/css/style.css' : 'static/src/styl/style.styl'
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
                src: 'static/src/css/style.css',
                dest: 'static/css/'
            }
        },

        imagemin: {
            dynamic: {
                files: [{
                    expand: true,
                    cwd: 'static/images/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: 'static/images/'
                },
                {
                    expand: true,
                    cwd: 'static/files/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: 'static/files/'
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
                files: ['static/images/**/*.{png,jpg,gif}', 'static/images/*.{png,jpg,gif}', 'static/files/*.{png,jpg,gif}'],
                tasks: ['imagemin'],
            }
        }

    });

    require('load-grunt-tasks')(grunt);


    grunt.registerTask('run', ['imagemin', 'stylus', 'autoprefixer', 'watch']);
    grunt.registerTask('default', ['run'])

};