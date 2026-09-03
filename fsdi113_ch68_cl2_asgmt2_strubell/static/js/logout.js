function openLogoutModal() {
    const modal = document.getElementById('logoutModal');
    modal.classList.remove('fade-out');
    modal.style.display = 'flex';
}

function closeLogoutModal() {
    const modal = document.getElementById('logoutModal');
    modal.classList.add('fade-out');
    setTimeout(function () {
        modal.style.display = 'none';
        modal.classList.remove('fade-out');
    }, 200); // MATCH sgngModalFadeOut DURATION
}

/* AUTO-CLOSE MODAL AFTER LOGOUT REDIRECT */
document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById('logoutModal');

    // IF USER IS NOT AUTHENTICATED, HIDE THE MODAL (BECAUSE LOGOUT ALREADY HAPPENED)
    if (!document.body.classList.contains('authenticated')) {
        modal.style.display = 'none';
    }
});
