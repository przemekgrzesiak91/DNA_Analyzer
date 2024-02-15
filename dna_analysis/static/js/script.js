function deleteProject(projectId) {
    $.ajax({
        url: '/project/' + projectId + '/delete/',
        type: 'POST',
        headers: {
        'X-CSRFToken': getCSRFToken() // Przekazanie tokena CSRF jako nagłówek HTTP
    },
    data: {
        // Dane żądania
    },
    success: function(response) {
            location.reload(); // Odśwież stronę

        // Obsługa sukcesu
    },
    error: function(xhr, textStatus, errorThrown) {
        // Obsługa błędu
    }
    });
}


function getCSRFToken() {
    var csrfToken = null;
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            csrfToken = cookie.substring('csrftoken='.length, cookie.length);
            break;
        }
    }
    return csrfToken;
}