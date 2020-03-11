const editButton = $('.ud-button-edit');
const deleteButton = $('.ud-button-delete');

editButton.click(function (e) {
    e.preventDefault();
    swal({
        title: "Are you sure?",
        text: "You really want to edit this thing?",
        icon: "warning",
        buttons: true,
    })
        .then((willEdit) => {
            if (willEdit) {
                swal("Taking you to the edit page", {
                    icon: "success",
                });
                location.href = this.href
            } else {
                swal("You've chosen to leave it as it is!");
            }
        });
})

deleteButton.click(function (e) {
    e.preventDefault();
    swal({
        title: "Are you sure?",
        text: "Are you super sure you want to delete this?",
        icon: "warning",
        buttons: true,
    })
        .then((willDelete) => {
            if (willDelete) {
                swal("Deleted from the database", {
                    icon: "success",
                });
                location.href = this.href
            } else {
                swal("You've let this one live!");
            }
        });
})

$(document).ready(function () {
    if ($(".swal-create-account").length) {
        swal({
            title: "Hey!",
            text: "Please register an account to view our beers!",
            icon: "warning",
        })
    }
})