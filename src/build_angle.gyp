# Copyright (c) 2010 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'translator_common',
      'type': 'static_library',
      'include_dirs': [
        '.',
        '../include',
      ],
      'variables': {
        'glslang_cpp_file': '<(INTERMEDIATE_DIR)/glslang.cpp',
        'glslang_tab_cpp_file': '<(INTERMEDIATE_DIR)/glslang_tab.cpp',
        'glslang_tab_h_file': '<(INTERMEDIATE_DIR)/glslang_tab.h',
      },
      'sources': [
        'compiler/BaseTypes.h',
        'compiler/Common.h',
        'compiler/ConstantUnion.h',
        'compiler/debug.cpp',
        'compiler/debug.h',
        'compiler/InfoSink.cpp',
        'compiler/InfoSink.h',
        'compiler/Initialize.cpp',
        'compiler/Initialize.h',
        'compiler/InitializeDll.cpp',
        'compiler/InitializeDll.h',
        'compiler/InitializeGlobals.h',
        'compiler/InitializeParseContext.h',
        'compiler/Intermediate.cpp',
        'compiler/intermediate.h',
        'compiler/intermOut.cpp',
        'compiler/IntermTraverse.cpp',
        'compiler/localintermediate.h',
        'compiler/MMap.h',
        'compiler/osinclude.h',
        'compiler/parseConst.cpp',
        'compiler/ParseHelper.cpp',
        'compiler/ParseHelper.h',
        'compiler/PoolAlloc.cpp',
        'compiler/PoolAlloc.h',
        'compiler/QualifierAlive.cpp',
        'compiler/QualifierAlive.h',
        'compiler/RemoveTree.cpp',
        'compiler/RemoveTree.h',
        'compiler/ShaderLang.cpp',
        'compiler/ShHandle.h',
        'compiler/SymbolTable.cpp',
        'compiler/SymbolTable.h',
        'compiler/Types.h',
        'compiler/unistd.h',
        'compiler/preprocessor/atom.c',
        'compiler/preprocessor/atom.h',
        'compiler/preprocessor/compile.h',
        'compiler/preprocessor/cpp.c',
        'compiler/preprocessor/cpp.h',
        'compiler/preprocessor/cppstruct.c',
        'compiler/preprocessor/memory.c',
        'compiler/preprocessor/memory.h',
        'compiler/preprocessor/parser.h',
        'compiler/preprocessor/preprocess.h',
        'compiler/preprocessor/scanner.c',
        'compiler/preprocessor/scanner.h',
        'compiler/preprocessor/slglobals.h',
        'compiler/preprocessor/symbols.c',
        'compiler/preprocessor/symbols.h',
        'compiler/preprocessor/tokens.c',
        'compiler/preprocessor/tokens.h',
        # Generated files
        '<(glslang_cpp_file)',
        '<(glslang_tab_cpp_file)',
        '<(glslang_tab_h_file)',
      ],
      'conditions': [
        ['OS=="win"', {
          'sources': ['compiler/ossource_win.cpp'],
        }, { # else: posix
          'sources': ['compiler/ossource_posix.cpp'],
        }],
      ],
      'actions': [
        {
          'action_name': 'flex_glslang',
          'inputs': ['compiler/glslang.l'],
          'outputs': ['<(glslang_cpp_file)'],
          'action': [
            'flex',
            '--noline',
            '--nounistd',
            '--outfile=<(glslang_cpp_file)',
            '<(_inputs)',
          ],
          'message': 'Executing flex on <(_inputs)',
        },
        {
          'action_name': 'bison_glslang',
          'inputs': ['compiler/glslang.y'],
          'outputs': ['<(glslang_tab_cpp_file)', '<(glslang_tab_h_file)'],
          'action': [
            'bison',
            '--no-lines',
            '--defines=<(glslang_tab_h_file)',
            '--skeleton=yacc.c',
            '--output=<(glslang_tab_cpp_file)',
            '<(_inputs)',
          ],
          'message': 'Executing bison on <(_inputs)',
        },
      ],
    },
    {
      'target_name': 'translator_glsl',
      'type': 'static_library',
      'dependencies': ['translator_common'],
      'include_dirs': [
        '.',
        '../include',
      ],
      'sources': [
        'compiler/CodeGenGLSL.cpp',
        'compiler/OutputGLSL.cpp',
        'compiler/OutputGLSL.h',
        'compiler/TranslatorGLSL.cpp',
        'compiler/TranslatorGLSL.h',
      ],
    },
    {
      'target_name': 'translator_hlsl',
      'type': 'static_library',
      'dependencies': ['translator_common'],
      'include_dirs': [
        '.',
        '../include',
      ],
      'sources': [
        'compiler/CodeGenHLSL.cpp',
        'compiler/OutputHLSL.cpp',
        'compiler/OutputHLSL.h',
        'compiler/TranslatorHLSL.cpp',
        'compiler/TranslatorHLSL.h',
        'compiler/UnfoldSelect.cpp',
        'compiler/UnfoldSelect.h',
      ],
    },
  ],
  'conditions': [
    ['OS=="win"', {
      'targets': [
        {
          'target_name': 'libGLESv2',
          'type': 'shared_library',
          'dependencies': ['translator_hlsl'],
          'include_dirs': [
            '.',
            '../include',
            '$(DXSDK_DIR)/include',
          ],
          'sources': [
            'common/angleutils.h',
            'common/debug.cpp',
            'common/debug.h',
            'libGLESv2/geometry/backend.cpp',
            'libGLESv2/geometry/backend.h',
            'libGLESv2/geometry/dx9.cpp',
            'libGLESv2/geometry/dx9.h',
            'libGLESv2/geometry/IndexDataManager.cpp',
            'libGLESv2/geometry/IndexDataManager.h',
            'libGLESv2/geometry/vertexconversion.h',
            'libGLESv2/geometry/VertexDataManager.cpp',
            'libGLESv2/geometry/VertexDataManager.h',
            'libGLESv2/Blit.cpp',
            'libGLESv2/Blit.h',
            'libGLESv2/Buffer.cpp',
            'libGLESv2/Buffer.h',
            'libGLESv2/Context.cpp',
            'libGLESv2/Context.h',
            'libGLESv2/Framebuffer.cpp',
            'libGLESv2/Framebuffer.h',
            'libGLESv2/libGLESv2.cpp',
            'libGLESv2/libGLESv2.def',
            'libGLESv2/main.cpp',
            'libGLESv2/main.h',
            'libGLESv2/mathutil.h',
            'libGLESv2/Program.cpp',
            'libGLESv2/Program.h',
            'libGLESv2/Renderbuffer.cpp',
            'libGLESv2/Renderbuffer.h',
            'libGLESv2/Shader.cpp',
            'libGLESv2/Shader.h',
            'libGLESv2/Texture.cpp',
            'libGLESv2/Texture.h',
            'libGLESv2/utilities.cpp',
            'libGLESv2/utilities.h',
          ],
          'msvs_settings': {
            'VCLinkerTool': {
              'AdditionalLibraryDirectories': ['$(DXSDK_DIR)/lib/x86'],
              'AdditionalDependencies': ['d3dx9.lib'],
            }
          },
        },
        {
          'target_name': 'libEGL',
          'type': 'shared_library',
          'dependencies': ['libGLESv2'],
          'include_dirs': [
            '.',
            '../include',
          ],
          'sources': [
            'common/angleutils.h',
            'common/debug.cpp',
            'common/debug.h',
            'libEGL/Config.cpp',
            'libEGL/Config.h',
            'libEGL/Display.cpp',
            'libEGL/Display.h',
            'libEGL/libEGL.cpp',
            'libEGL/libEGL.def',
            'libEGL/main.cpp',
            'libEGL/main.h',
            'libEGL/Surface.cpp',
            'libEGL/Surface.h',
          ],
          'msvs_settings': {
            'VCLinkerTool': {
              'AdditionalDependencies': ['d3d9.lib'],
            }
          },
        },
      ],
    }],
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
