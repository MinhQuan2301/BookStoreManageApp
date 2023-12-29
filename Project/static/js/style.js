document.addEventListener('DOMContentLoaded', function () {
        var body = document.body;
        var darkModeToggle = document.querySelector('.dark-mode-toggle');

        function toggleDarkMode() {
            body.classList.toggle('dark-mode');
            var isDarkMode = body.classList.contains('dark-mode');
            localStorage.setItem('darkMode', isDarkMode);
        }

        darkModeToggle.addEventListener('click', toggleDarkMode);
        var isDarkMode = localStorage.getItem('darkMode') === 'true';
        if (isDarkMode) {
            body.classList.add('dark-mode');
        }
        window.addEventListener('pageshow', function (event) {
            var isDarkMode = localStorage.getItem('darkMode') === 'true';
            if (isDarkMode) {
                body.classList.add('dark-mode');
            } else {
                body.classList.remove('dark-mode');
            }
        });
    });
function handleViewDetailClick(name, image, info) {
    // Hiển thị overlay
    var detailOverlay = document.getElementById('detailOverlay');
    detailOverlay.style.display = 'block';

    // Cập nhật nội dung chi tiết
    document.getElementById('detailName').textContent = name;
    document.getElementById('detailImage').src = image;
    document.getElementById('detailInfo').textContent = info;
}
function closeDetailOverlay() {
    var detailOverlay = document.getElementById('detailOverlay');
    detailOverlay.style.display = 'none';
}
