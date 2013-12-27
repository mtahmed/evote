$("#txtStartDate").datepicker();
$("#txtEndDate").datepicker();
AddQuestion(1);

function AddOption(question_number, option_number) {
    var outer_div = document.getElementById("divQuestion" + question_number + "Options");
    var inner_div = document.createElement("div");
    inner_div.id = "divQuestion" + question_number + "Option" + option_number;
    
    var newOption = document.createElement("input");
    newOption.type = "text";
    newOption.className = "textfield";
    newOption.id = "txtQuestion" + question_number + "Option" + option_number;
    inner_div.appendChild(newOption);
    
    var remove_button = document.createElement("input");
    remove_button.type = "button";
    remove_button.value = "Remove";
    remove_button.id = "btnRemove" + question_number + "Option" + option_number;
    remove_button.onclick = function () { RemoveOption(question_number, option_number); };
    inner_div.appendChild(remove_button);
    
    outer_div.appendChild(inner_div);
    
    document.getElementById("btnQuestion" + question_number + "AddOption").onclick = function() { AddOption(question_number, option_number + 1); };
}

function RemoveOption(question_number, option_number) {
    document.getElementById("divQuestion" + question_number + "Option" + option_number).style.display = "none";
}

function AddQuestion(question_number) {
    var outer_div = document.createElement("div");
    outer_div.className = "two-columns";
    outer_div.id = "divQuestion" + question_number;
    document.getElementById("divQuestions").appendChild(outer_div);
    
    CreateQuestionHeader(question_number);
    
    var title_div = document.createElement("div");
    var title = document.createElement("div");
    title.innerHTML = "Question title: ";
    title_div.appendChild(title);
    title = document.createElement("div");
    var textbox = document.createElement("textarea");
    textbox.id = "txtQuestion" + question_number + "Title";
    textbox.className = "textfield";
    textbox.style.minHeight = "50px";
    textbox.style.minWidth = "100px";
    title.appendChild(textbox);
    title_div.appendChild(title);
    outer_div.appendChild(title_div);
    
    CreateOptionSection(question_number);
    
    var divOuterButton = document.createElement("div")
    divOuterButton.appendChild(document.createElement("div"));
    var divButton = document.createElement("div");
    var button = document.createElement("input");
    button.type = "button";
    button.id = "btnQuestion" + question_number + "AddOption";
    button.value = "Add option";
    divButton.appendChild(button);
    divOuterButton.appendChild(divButton);
    outer_div.appendChild(divOuterButton);
    
    document.getElementById("btnAddQuestion").onclick = function () { AddQuestion(question_number + 1); };
    document.getElementById("btnQuestion" + question_number + "AddOption").onclick = function () { AddOption(question_number, 3); };
}

function CreateQuestionHeader(question_number) {
     var outer_div = document.getElementById("divQuestion" + question_number);
     
     var div = document.createElement("div");
     div.className = "question-header";
     div.innerHTML = "Question " + question_number + ": ";
     
     if(question_number > 1) {
         var button = document.createElement("input");
         button.type = "button";
         button.onclick = function () { RemoveQuestion(question_number); };
         button.value = "Remove";
         div.appendChild(button);
     }
     
     outer_div.appendChild(div);
}

function CreateOptionSection(question_number) {
    var outermost_div = document.getElementById("divQuestion" + question_number);
    var outer_div = document.createElement("div");
    
    var option_title = document.createElement("div");
    option_title.innerHTML = "Options: ";
    
    var divOptions = document.createElement("div");
    divOptions.className = "poll-options";
    divOptions.id = "divQuestion" + question_number + "Options";
    
    for(var i = 1; i < 3; i++) {
        var tempDiv = document.createElement("div");
        tempDiv.id = "divQuestion" + question_number + "Option" + i;
        
        var inputField = document.createElement("input");
        inputField.className = "textfield";
        inputField.id = "txtQuestion" + question_number + "Option" + i;
        
        tempDiv.appendChild(inputField);
        divOptions.appendChild(tempDiv);
    }
    
    outer_div.appendChild(option_title);
    outer_div.appendChild(divOptions);
    
    outermost_div.appendChild(outer_div);
}

function RemoveQuestion(question_number) {
    document.getElementById("divQuestion" + question_number).style.display = "none";
}
