// Get modal elements
const modal = document.getElementById("imgModal");
const modalImg = document.getElementById("modalImg");
const modalClose = document.getElementById("modalClose");
// Add click event to all gallery images
document.querySelectorAll(".gallery-image").forEach((img) => {
  img.addEventListener("click", function () {
    modal.style.display = "flex";
    modalImg.src = this.src;
    modalImg.alt = this.alt;
  });
});
// Close modal on click of close button or outside image
modalClose.onclick = function () {
  modal.style.display = "none";
  modalImg.src = "";
};
modal.onclick = function (e) {
  if (e.target === modal) {
    modal.style.display = "none";
    modalImg.src = "";
  }
};
