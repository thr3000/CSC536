<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Goal Tracker App</title>
    <!-- Add Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KyZXEAg3QhqLMpG8r+Knujsl7/1L_dstPt3HV5HzF6Gvk/e3s4Wz6iJgD/+ub2oU"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <div class="container mt-5">
      <h1 class="text-center mb-4">Create a New Goal</h1>
      <div id="goalsContainer">
        <!-- Goal Form Template -->
        <div id="goalFormTemplate" style="display: none;">
          <div class="goal mb-4">
            <div class="mb-3">
              <label for="goalTitle" class="form-label">Goal Title</label>
              <input
                type="text"
                class="form-control"
                name="goalTitle"
                placeholder="Enter your goal title"
              />
            </div>
            <div class="subgoalsContainer"></div>
            <button type="button" class="btn btn-secondary mb-3" onclick="addSubgoal(this)">Add Subgoal</button>
          </div>
        </div>
      </div>
      <button type="button" class="btn btn-primary mb-3" onclick="addGoal()">Add Goal</button>
      <button type="submit" class="btn btn-primary" onclick="createGoal()">Create Goal</button>
    </div>
    <!-- Add Bootstrap JS -->
    <script
      src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"
      integrity="sha384-oBqDVmMz4fnFO9gybBud7TlRbs/ic4AwGcFZOxg5DpPt8EgeUIgIwzjWfXQKWA3"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"
      integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/"
      crossorigin="anonymous"
    ></script>
    <script>
      function addGoal() {
        const goalsContainer = document.getElementById('goalsContainer');
        if (goalsContainer.children.length === 0) {
          // Show the "Add Goal" button
          document.querySelector('.btn-primary').style.display = 'block';
        }
        const goalFormTemplate = document.getElementById('goalFormTemplate');
        const newGoal = goalFormTemplate.cloneNode(true);
        newGoal.removeAttribute('id');
        newGoal.style.display = 'block';
        goalsContainer.appendChild(newGoal);
      }

      function addSubgoal(button) {
        const goalContainer = button.closest('.goal');
        const subgoalsContainer = goalContainer.querySelector('.subgoalsContainer');
        const newSubgoal = document.createElement('div');
        newSubgoal.classList.add('subgoal', 'mb-3');
        newSubgoal.innerHTML = `
          <label for="subgoal" class="form-label">Subgoal</label>
          <textarea
            class="form-control"
            name="subgoal"
            rows="3"
            placeholder="Enter your subgoal"
          ></textarea>
          <div class="mb-3">
            <label for="timelineDate" class="form-label">Timeline Date</label>
            <input
              type="date"
              class="form-control"
              name="timelineDate"
              placeholder="Select date"
            />
          </div>
          <div class="mb-3">
            <label for="timelineTime" class="form-label">Timeline Time</label>
            <input
              type="time"
              class="form-control"
              name="timelineTime"
              placeholder="Select time"
            />
          </div>
        `;
        subgoalsContainer.appendChild(newSubgoal);
      }

      function createGoal() {
        const goals = document.querySelectorAll('.goal');
        goals.forEach((goal, index) => {
          const goalTitle = goal.querySelector('[name="goalTitle"]').value;
          console.log(`Goal ${index + 1}: ${goalTitle}`);
          const subgoals = goal.querySelectorAll('.subgoal');
          subgoals.forEach((subgoal, subIndex) => {
            const subgoalTitle = subgoal.querySelector('[name="subgoal"]').value;
            const timelineDate = subgoal.querySelector('[name="timelineDate"]').value;
            const timelineTime = subgoal.querySelector('[name="timelineTime"]').value;
            console.log(`  Subgoal ${subIndex + 1}: ${subgoalTitle}`);
            console.log(`  Timeline Date: ${timelineDate}`);
            console.log(`  Timeline Time: ${timelineTime}`);
          });
        });
      }
    </script>
  </body>
</html>
