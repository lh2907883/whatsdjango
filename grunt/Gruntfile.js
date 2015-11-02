'use strict';

module.exports = function (grunt) {

  // Time how long tasks take. Can help when optimizing build times
  require('time-grunt')(grunt);

  // Load grunt tasks automatically
  require('load-grunt-tasks')(grunt);

  var config = {
    'app': '../whatsdjango',
    'devstatic': '../whatsdjango/devstatic',
    'static': '../whatsdjango/static'
  };
  
  // Define the configuration for all the tasks
  grunt.initConfig({

    // Project settings
    config: config,

    // 监视html,js,css文件改变,执行对应任务
    watch: {
      js: {
        files: [
          '<%= config.devstatic %>/**/*.js', 
          //'!<%= config.devstatic %>/js/lib/**/*.js'
        ],
        tasks: ['copy:js'/*,'jshint'*/],
        options: {
          livereload: true
        }
      },
      // gruntfile: {
      //   files: ['Gruntfile.js']
      // },
      less: {
        files: [
          '<%= config.devstatic %>/**/*.less'
        ],
        tasks: ['less:debug'],
        options: {
          livereload: true
        }
      },
      livereload: {
        options: {
          livereload: true
        },
        files: [
          '<%= config.app %>/**/*.html',
          '<%= config.devstatic %>/**/*.js',
          '<%= config.devstatic %>/**/*.css',
          '<%= config.devstatic %>/images/{,*/}*'
        ]
      }
    },

    // js代码规范检查
    jshint: {
      options: {
        jshintrc: '.jshintrc',
        reporter: require('jshint-stylish')
      },
      all: [
        'Gruntfile.js',
        '<%= config.devstatic %>/**/*.js'
        //'!<%= config.devstatic %>/js/lib/*'
      ]
    }, 
    
    // less文件编译
    less: {
      debug: {
        options: {
          compress: false,
          sourceMap: false,
          yuicompress: false
        },
        files: [{
          expand: true,
          cwd: '<%= config.devstatic %>',
          src: [
            '**/*.less'
          ],
          dest: '<%= config.static %>',
          ext: '.css'
        }]
      },
      'export': {
        options: {
          compress: true,
          sourceMap: false,
          yuicompress: false
        },
        files: [{
          expand: true,
          cwd: '<%= config.devstatic %>',
          src: [
            '**/*.less'
          ],
          dest: '<%= config.static %>',
          ext: '.css'
        }]
      }
    },    

    //css压缩
    cssmin: {
      prod: {
        options: {
          report: 'gzip'
        },
        files: [{
          expand: true,
          cwd: '<%= config.static %>',
          src: [
            '**/*.css'
          ],
          dest: '<%= config.static %>'
        }]
      }
    },

    //js压缩
    uglify: {
      dist: {
        files: [{
          expand:true,
          cwd:'<%= config.devstatic %>', 
          src:[
            '**/*.js'
            //'!lib/*'
          ],
          dest: '<%= config.static %>' 
        }]
      }
    },

    // 导出项目时用到的copy任务(复制文件和文件夹)
    copy: {
      js: {
        files: [{
          expand: true,
          dot: true,
          cwd: '<%= config.devstatic %>',
          dest: '<%= config.static %>',
          src: [
            '**/*.js'
            // '!less{,/*}',
            // '!css{,/*}/*'
          ]
        }]
      }
    },

    //文件内容替换(php模板可能会用到)
    // regexReplace: {
    //   dist: {
    //     options: {
    //       //在文本中使用下面的正则替换内容( 例:把'href="scripts'正则匹配到的内容替换成字符串'href="__RESOURCES_PHONE__/scripts' )
    //       regex: {
    //         'href="scripts': 'href="__RESOURCES_PHONE__/scripts',
    //         'src="scripts': 'src="__RESOURCES_PHONE__/scripts',
    //         'href="styles': 'href="__RESOURCES_PHONE__/styles',
    //         'src="images': 'src="__RESOURCES_PHONE__/images'
    //       }
    //     },
    //     files: [{
    //       expand: true,
    //       cwd: '<%= config.app %>',
    //       src: '*.html',
    //       dest: '<%= config.export %>',
    //       ext: '.html'
    //     }]
    //   }
    // }
  });

  /**
   * 生成
   */
  grunt.registerTask('build', [
    'less:debug',
    'copy:js'
  ]);

  /**
   * 导出任务
   */
  grunt.registerTask('export', [
    'less:export',
    'uglify'
    // 'regexReplace',
    // 'cssmin'
  ]);

  /**
   * (默认任务)
   * watch 
   */
  grunt.registerTask('default', [
    'build',
    'watch'
  ]);
};
