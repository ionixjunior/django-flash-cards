document.addEventListener('DOMContentLoaded', (event) => {
    const flashcard = document.querySelector('.flash-card');

    if (flashcard) {
        flashcard.addEventListener('click', () => {
            if (!flashcard.classList.contains('is-flipped')) {
                flashcard.classList.add('is-flipped');
            }
        });
    }
});