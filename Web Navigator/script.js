const Stack = require('./Stack.js');
const prompt = require('prompt-sync')();
// ------------------------------
// Initialization
const backPages = new Stack()
const nextPages= new Stack()
let currentPage = "HI welcome to our world"
// ------------------------------

// ------------------------------
// Helper Functions
const showCurrentPage = (action)=>{
  console.log(${action})
  console.log(currentPage)
  console.log(backPages.peek())
  console.log(nextPages.peek())
}
const newPage = (page)=>{
  backPages.push(currentPage)
  currentPage =page
  while (!nextPages.isEmpty()){
    nextPages.pop()
  }
  showCurrentPage("NEW: ")
}
const backPage = ()=>{
  nextPages.push(currentPage)
  currentPage =backPages.pop()
  showCurrentPage("BACK:")
}
const nextPage = ()=>{
  backPages.push(currentPage)
  currentPage = nextPages.pop()
  showCurrentPage("NEXT:")
}
// ------------------------------
let finish = false
let showBack = false
let showNext = false 
/*
 * The following strings are used to prompt the user
 */
const baseInfo = '\nEnter a url';
const backInfo = 'B|b for back page';
const nextInfo = 'N|n for next page';
const quitInfo = 'Q|q for quit';
const question = 'Where would you like to go today? '

// ------------------------------
// User Interface Part 1
// ------------------------------
showCurrentPage('DEFAULT: ')
while (!finish){
  let instruction = baseInfo
  if (backPages.peek() !== null){
    instruction += `, ${backInfo}`
    showBack = true
  }else{
    showBack = false
  }
  if (nextPages.peek()!= null){
    instruction += `, ${nextInfo}`
    showNext = true
  }else
  {
    showNext= false
  }
  instruction += `, ${quitInfo}`
  console.log(instruction)
  const answer = prompt(question)
  const lowerCaseAnswer = answer.toLowerCase()
  if ((lowerCaseAnswer !== 'n')&& (lowerCaseAnswer !== 'b') && (lowerCaseAnswer !=='q')){
    newPage(answer)
  }else if ((lowerCaseAnswer == 'b')&& (showBack===true)){
    backPage()
  }else if( (lowerCaseAnswer =='n')&& (showNext === true)){
    nextPage()
  }else if (lowerCaseAnswer === 'b') {
    // invalid input to a non-available option
    console.log('Cannot go back a page. Stack is empty.');
  } else if (lowerCaseAnswer === 'n') {
    // invalid input to a non-available option
    console.log('Cannot go to the next page. Stack is empty.');
  }else if (lowerCaseAnswer == 'q'){
    finish = true
  }

}
  