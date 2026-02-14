document.addEventListener("DOMContentLoaded", function () {
    const deleteLinks = document.querySelectorAll("a.btn-danger");

    deleteLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            if (!confirm("¿Estás seguro de que deseas eliminar este ticket?")) {
                e.preventDefault();
            }
        });
    });
});
