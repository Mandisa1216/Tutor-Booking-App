



// Get all the confirm buttons
const confirmButtons = document.querySelectorAll('.confirm-btn');

// Add a click event listener to each confirm button
confirmButtons.forEach((button, index) => {
  button.addEventListener('click', () => {
    // Get the status cell corresponding to the clicked button
    const statusCell = document.querySelectorAll('.status-cell')[index];

    // Change the text and color of the status cell
    statusCell.textContent = 'Confirmed';
    statusCell.style.color = 'green';
  });
});



  // JavaScript to display modal and handle confirmation
  document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('myModal');
    var deleteForm = document.getElementById('deleteForm');
    var confirmButton = document.getElementById('confirmDelete');
    var cancelButton = document.getElementById('cancelDelete');

    // Show modal when form is submitted
    deleteForm.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent the form from submitting
      modal.style.display = 'block';
    });

    // Handle delete confirmation
    confirmButton.addEventListener('click', function() {
      deleteForm.submit(); // Submit the form for actual deletion
    });

    // Handle cancel action
    cancelButton.addEventListener('click', function() {
      modal.style.display = 'none'; // Hide the modal
    });
  });
