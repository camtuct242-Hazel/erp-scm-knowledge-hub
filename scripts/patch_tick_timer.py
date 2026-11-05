with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

target = """        // Start countdown timer
        if (state.timerInterval) clearInterval(state.timerInterval);
        state.timerInterval = setInterval(() => {
          state.timerSeconds--;
          this.tickTimer();
        }, 1000);"""

repl = """        // Start countdown timer
        if (state.timerInterval) clearInterval(state.timerInterval);
        state.timerInterval = setInterval(() => {
          this.tickTimer();
        }, 1000);"""

target_tick = """    tickTimer: function() {
      const minutes = Math.floor(state.timerSeconds / 60);
      const seconds = state.timerSeconds % 60;
      const str = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
      const timerDisplay = document.getElementById('active-timer-display');
      if (timerDisplay) timerDisplay.innerText = str;

      if (state.timerSeconds <= 300) {
        const tb = document.getElementById('active-timer-box');
        if (tb) tb.classList.add('warning');
      }

      if (state.timerSeconds <= 0) {
        clearInterval(state.timerInterval);
        this.submitExamNow();
      }
    },"""

repl_tick = """    tickTimer: function() {
      if (state.timerSeconds > 0) {
        state.timerSeconds--;
      }
      const minutes = Math.floor(state.timerSeconds / 60);
      const seconds = state.timerSeconds % 60;
      const str = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
      const timerDisplay = document.getElementById('active-timer-display');
      if (timerDisplay) timerDisplay.innerText = str;

      if (state.timerSeconds <= 300) {
        const tb = document.getElementById('active-timer-box');
        if (tb) tb.classList.add('warning');
      }

      if (state.timerSeconds <= 0) {
        if (state.timerInterval) clearInterval(state.timerInterval);
        this.submitExamNow();
      }
    },"""

if target in code:
    code = code.replace(target, repl)
if target_tick in code:
    code = code.replace(target_tick, repl_tick)

with open('outputs/app/app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("tickTimer updated successfully in app.js!")
