document.addEventListener("DOMContentLoaded", () => {
  const optimizeBtn = document.getElementById("optimizeBtn");
  const queryInput = document.getElementById("queryInput");
  const resultElement = document.getElementById("result");

  optimizeBtn.addEventListener("click", optimizeQuery);

  async function optimizeQuery() {
      const query = queryInput.value.trim();
      if (!query) {
          alert("Please enter a query to optimize.");
          return;
      }

      try {
          const response = await fetch('/optimization', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/x-www-form-urlencoded',
              },
              body: `text=${JSON.stringify(query)}`
          });

          if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
          }

          const result = await response.text();
          resultElement.textContent = result;
      } catch (error) {
          console.error("Error:", error);
          resultElement.textContent = "An error occurred while optimizing the query.";
      }
  }
});