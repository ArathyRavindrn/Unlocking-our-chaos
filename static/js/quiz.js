(function () {
  'use strict';

  const config = window.quizConfig;
  if (!config || !config.questions || !config.wrongMessages) return;

  const questions = config.questions;
  const wrongMessages = config.wrongMessages;
  let currentIndex = 0;

  const introScreen = document.getElementById('intro-screen');
  const quizScreen = document.getElementById('quiz-screen');
  const successScreen = document.getElementById('success-screen');
  const wrongModal = document.getElementById('wrong-modal');
  const modalTitle = wrongModal.querySelector('.modal-title');
  const modalMessage = wrongModal.querySelector('.modal-message');
  const tryAgainBtn = wrongModal.querySelector('.btn-try-again');

  const questionLabel = quizScreen.querySelector('.question-label');
  const qNumSpan = quizScreen.querySelector('.q-num');
  const qEmojiSpan = quizScreen.querySelector('.q-emoji');
  const questionTextEl = quizScreen.querySelector('.question-text');
  const optionsContainer = quizScreen.querySelector('.options');

  function showScreen(screen) {
    document.querySelectorAll('.screen').forEach(function (el) {
      el.classList.remove('active');
    });
    if (screen && screen.classList) screen.classList.add('active');
  }

  function showIntro() {
    showScreen(introScreen);
  }

  function showQuiz() {
    showScreen(quizScreen);
    currentIndex = 0;
    renderQuestion();
  }

  function renderQuestion() {
    const q = questions[currentIndex];
    if (!q) {
      showSuccess();
      return;
    }
    qNumSpan.textContent = q.number;
    qEmojiSpan.textContent = q.emoji || '❤️';
    questionTextEl.textContent = q.text;
    optionsContainer.innerHTML = '';
    q.options.forEach(function (opt, i) {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'option-btn';
      btn.textContent = opt;
      btn.dataset.index = String(i);
      btn.addEventListener('click', function () {
        handleAnswer(parseInt(btn.dataset.index, 10));
      });
      optionsContainer.appendChild(btn);
    });
  }

  function handleAnswer(selectedIndex) {
    const q = questions[currentIndex];
    const correct = q.correct;
    if (selectedIndex === correct) {
      // Reveal only the current image (based on currentIndex)
      const imageCells = document.querySelectorAll('.img-cell');
      if (currentIndex < imageCells.length) {
        imageCells[currentIndex].classList.add('reveal');
      }
      
      currentIndex++;
      if (currentIndex >= questions.length) {
        // Delay before showing success screen (after 4th image is revealed)
        setTimeout(function () {
          showSuccess();
        }, 2000);
      } else {
        renderQuestion();
      }
      return;
    }
    showWrongModal();
  }

  function showWrongModal() {
    const msg = wrongMessages[Math.floor(Math.random() * wrongMessages.length)];
    modalTitle.textContent = msg.title;
    modalMessage.textContent = msg.message;
    tryAgainBtn.textContent = msg.button;
    wrongModal.classList.remove('hidden');
  }

  function hideWrongModal() {
    wrongModal.classList.add('hidden');
  }

  function showSuccess() {
    showScreen(successScreen);
  }

  // Intro: Yes -> quiz
  const yesBtn = document.querySelector('.btn-yes');
  if (yesBtn) {
    yesBtn.addEventListener('click', function () {
      showQuiz();
    });
  }

  // Intro: No -> gentle nudge, then restore label
  const noBtn = document.querySelector('.btn-no');
  if (noBtn) {
    noBtn.addEventListener('click', function () {
      var initial = noBtn.getAttribute('data-initial') || 'No 😔';
      noBtn.textContent = 'Sure? Click Yes 🥰';
      setTimeout(function () {
        noBtn.textContent = initial;
      }, 1500);
    });
  }

  tryAgainBtn.addEventListener('click', hideWrongModal);
  wrongModal.addEventListener('click', function (e) {
    if (e.target === wrongModal) hideWrongModal();
  });
})();
