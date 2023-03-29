###################################SummerNote ConfigS###########################################################
# django-summernote
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

SUMMERNOTE_THEME = 'bs4'  # Show summernote with Bootstrap4

X_FRAME_OPTIONS = 'SAMEORIGIN'

SUMMERNOTE_CONFIG = { 
    
    # Using SummernoteWidget - iframe mode, default
    'iframe': True,

    'summernote' : {
        # Define height and width here
        # 'width': '50%',
        # 'height': '720',
        
         # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline']],
            ['script', ['strikethrough', 'superscript', 'subscript']],
            ['paragraph style', ['ol', 'ul', 'paragraph']],
            ['font2', ['fontname', 'fontsize', 'fontsizeunit']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['hr', ['hr']],
            ['maxm', ['fullscreen']],
            ['code', ['codeview']],
            ['clear', ['forecolor', 'backcolor', 'clear', 'color']],
            ['height', ['height']],
            ['solve', ['undo', 'redo']],
            ['help', ['help']],
        ],
        
        # You can also add custom settings for external plugins
        'print': {
            'stylesheetUrl': '/some_static_folder/printable.css',
        },
        
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            # # You have to include theme file in 'css' or 'css_for_inplace' before using it.
            # 'theme': 'monokai',
        },
    },
    # Require users to be authenticated for uploading attachments.
    'attachment_require_authentication': True,
    
    # You can completely disable the attachment feature.
    'disable_attachment': False,
    
    # Set to `True` to return attachment paths in absolute URIs.
    'attachment_absolute_uri': False,
    
    # Lazy initialization
    # If you want to initialize summernote at the bottom of page, set this as True
    # and call `initSummernote()` on your page.
    'lazy': True,
    
    # # To use external plugins,
    # # Include them within `css` and `js`.
    # 'js': {
    #     '/some_static_folder/summernote-ext-print.js',
    #     '//somewhere_in_internet/summernote-plugin-name.js',
    # },
}
#############################################################################################