$(document).ready( function () {
    $('#searchbar').keyup( function () {
        var sb
        sb = $(this).val()
        $.get('search/',{'searchbar': sb}, function (data) {
            $('#search_result').html(data)
        })
    })
})