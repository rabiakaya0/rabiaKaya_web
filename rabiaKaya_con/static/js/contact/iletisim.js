document.addEventListener("DOMContentLoaded", function () {
    const messageField = document.querySelector("[name='mesaj']");
    const charCount = document.getElementById("charCount");

    if (messageField) {
        messageField.setAttribute("maxlength", "500");  

        messageField.addEventListener("input", function () {
            const currentLength = messageField.value.length;
            charCount.textContent = `${currentLength} / 500`;
        });
    }
});