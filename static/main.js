function CopyToClipboard(){
    const copyText = document.getElementById("password-text")
    navigator.clipboard.writeText(copyText.innerHTML);
}