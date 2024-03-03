// This code removes unwanted options from the Quill Editor's Toolbar
var elementsToRemove = [
    '.ql-picker-label',
    '.ql-picker',
    '.ql-header',
    '.ql-color',
    '.ql-color-picker',
    '.ql-image',
    '.ql-video',
    '.ql-clean',
    '.ql-font'
];
  
for (var i = 0; i < elementsToRemove.length; i++) {
    var element = document.querySelector(elementsToRemove[i]);
    if (element) {
        element.remove();
    }
}  