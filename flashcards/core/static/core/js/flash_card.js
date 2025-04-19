document.addEventListener('DOMContentLoaded', (event) => {
    const flashcard = document.querySelector('.flash-card');

    if (flashcard) {
        flashcard.addEventListener('click', () => {
            flashcard.classList.toggle('is-flipped');
        });
    }
});