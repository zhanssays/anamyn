$(document).ready(function (e) {
    $("#tag_input").keyup(function (event) {
        if (event.which == 188) {
            createTag();
        }
        if (event.which == 8) {
            if ($(".tag_span").length == 0) {
                $("#tag_input").attr('placeholder', 'Введите тэги через запятую, например “пособие, семья”');
                $("#tag_input").removeClass('tag-input-small');
                $("#tag_input").addClass('tag-input-big');
            }
        }
    });
    $("#tag_input").keydown(function (event) {
        if (event.which == 8) {
            var value = $('#tag_input').val();
            if (value.length == 0) {
                deleteTag();
            }
        }
    });

    function createTag() {
        var value = $('#tag_input').val();
        var tag = value.split(",")[0];
        console.log(tag);
        if (tag.length > 0) {
            $('<span class="tag_span">' + tag + '</span>').insertBefore("#tag_input");
        }
        $('#tag_input').val("");
        $("#tag_input").attr('placeholder', 'Тэг');
        $("#tag_input").removeClass('tag-input-big');
        $("#tag_input").addClass('tag-input-small');
    }

    function deleteTag() {
        $(".tag_span").last().remove();
    }

    // ===========   TINYMCE ============
    tinymce.init({
        selector: '#mytextarea',
        toolbar: 'bold  italic underline | emoticons image ',
        menubar: false,
        branding: false,
        plugins: "emoticons image contextmenu media",
        image_dimensions: false,
        paste_data_image: true,
        file_picker_types: 'image',
        file_picker_callback: function (cb, value, meta) {
            var input = document.createElement('input');
            input.setAttribute('type', 'file');
            input.setAttribute('accept', 'image/*');

            /*
              Note: In modern browsers input[type="file"] is functional without
              even adding it to the DOM, but that might not be the case in some older
              or quirky browsers like IE, so you might want to add it to the DOM
              just in case, and visually hide it. And do not forget do remove it
              once you do not need it anymore.
            */

            input.onchange = function () {
                var file = this.files[0];

                var reader = new FileReader();
                reader.onload = function () {
                    /*
                      Note: Now we need to register the blob in TinyMCEs image blob
                      registry. In the next release this part hopefully won't be
                      necessary, as we are looking to handle it internally.
                    */
                    var id = 'blobid' + (new Date()).getTime();
                    var blobCache = tinymce.activeEditor.editorUpload.blobCache;
                    var base64 = reader.result.split(',')[1];
                    var blobInfo = blobCache.create(id, file, base64);
                    blobCache.add(blobInfo);

                    /* call the callback and populate the Title field with the file name */
                    cb(blobInfo.blobUri(), {title: file.name});
                };
                reader.readAsDataURL(file);
            };
            input.click();
        }
    });
});
