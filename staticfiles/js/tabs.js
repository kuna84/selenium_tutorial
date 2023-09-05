function openTab(tabName) {
  var i, tabs, buttons;
  tabs = document.getElementsByClassName("tab");
  buttons = document.getElementsByClassName("tab-buttons")[0].getElementsByTagName("button");
  for (i = 0; i < tabs.length; i++) {
    tabs[i].classList.remove("active");
    buttons[i].classList.remove("active");
  }
  document.getElementById(tabName).classList.add("active");
  event.currentTarget.classList.add("active");
}

window.addEventListener('DOMContentLoaded', function() {
  openTab('english-tab');
});