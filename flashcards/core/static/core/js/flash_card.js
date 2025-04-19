document.addEventListener('DOMContentLoaded', (event) => {
    const flashcard = document.querySelector('.flash-card');
    const feedbackButtons = document.querySelector('.feedback-buttons');

    if (flashcard && feedbackButtons) {
        flashcard.addEventListener('click', () => {
            if (!flashcard.classList.contains('is-flipped')) {
                flashcard.classList.add('is-flipped');
                feedbackButtons.style.display = 'block';
            }
        });
    }
});
