document.addEventListener('DOMContentLoaded', function () {
    const showMoreBtn = document.getElementById('show-more-btn');
    const hiddenItems = document.querySelectorAll('.list-item.hidden');

    if (showMoreBtn) {
        showMoreBtn.addEventListener('click', function () {
            hiddenItems.forEach(shoe => {
                shoe.classList.remove('hidden');
            });
            this.style.display = 'none'; // Hide the button after use
        });
    }
});