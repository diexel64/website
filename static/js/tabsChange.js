function openTab(tabName) {
      // Hide all tab content
      var tabContents = document.getElementsByClassName("tabcontent");
      for (var i = 0; i < tabContents.length; i++) {
        tabContents[i].style.display = "none";
      }

      // Deactivate all tab links
      var tabLinks = document.getElementsByClassName("tablink");
      for (var i = 0; i < tabLinks.length; i++) {
        tabLinks[i].classList.remove("active");
      }

      // Show the selected tab content and activate its corresponding tab link
      document.getElementById(tabName).style.display = "block";
      event.currentTarget.classList.add("active");
    }