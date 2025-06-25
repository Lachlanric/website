// Side panel toggle logic
const sidePanel = document.getElementById("sidePanel");
const sidePanelToggle = document.getElementById("sidePanelToggle");
sidePanelToggle.onclick = function () {
  sidePanel.classList.toggle("open");
  document.body.classList.toggle("panel-open");
};
