function ValidateNameField(s, a) {
    var invalidChar = false;
    var chars = [">", "<", "}", "/", "#", "!", "\"", "&", "&amp;", "&gt;", "&lt;", "&quot;"];

    var t = $('#' + s.id.replace('Validator', ''));

    //check field for invalid characters
    if (t != undefined && t.val() != null)
    {
        for (var i = 0; i < chars.length; i++) {
            if (t.val().indexOf(chars[i]) > -1) {
                invalidChar = true;
                break;
            }
        }
    }

    var c = $('#cbNo' + t.attr('id').replace('txt', ''));

    //if name field is null or contain invalid char(s) and checkbox is not checked
    if ((t.val() === '' || t.val() == 'undefined' || invalidChar) && !(c.is(':checked')))
    {
        a.IsValid = false; //name field is invalid
    }
    else
    {
        a.IsValid = true; //name field is valid
    }
}

function ConfirmNumberLostFocus(s, a) {
    var c = document.getElementById('txtCN');

    if (c.value.indexOf('2019') > -1) {
        if ($('#txtLastNameValidator') != null)
        { 
            $('#txtLastNameValidator')[0].innerHTML = "You must provide a valid Last/Family Name<br/>";
        }
    }
}

$(document).ready(function () {
    $('#ETNoLastName').hide();
    $('#NoLastName').hide();

    // Forgot confirmation num - program year click
    $('#2019PYLabel').click(function () {
        $('#txtLastName').attr('disabled', false);    
    });
});


