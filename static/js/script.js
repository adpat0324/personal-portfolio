document.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('play-button');
    if (btn) {
        btn.addEventListener('click', function () {
            if (btn.textContent === '▶') {
                btn.textContent = '❚❚';
            } else {
                btn.textContent = '▶';
            }
        });
    }
});
