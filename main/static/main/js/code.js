
let program = document.getElementById('prog');
let blog = document.getElementById('blogs');

if (program) {
  program.addEventListener("click", () => {
    document.getElementById("news").style.display = "none";
    document.getElementById("programmes").style.display = "block";
  });
}
if (blog) {
blog.addEventListener("click", () => {
    document.getElementById("news").style.display = "block";
    document.getElementById("programmes").style.display = "none";
});
}

