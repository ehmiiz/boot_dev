// js playground


function myFunnyLoop () {
    // let myVariable = 5

    const myArray = ['Emil', 'Larsson', 32]

    for (let i = 0; i < myArray.length; i++) {
        const element = myArray[i];
        const msg = `Loop element: ${i} \nHey, I'm ${myArray[0]} I'm ${myArray[2]} years old.`
        console.log(msg)
    }

    // lets do some math
    // the new keyword is 
    date = new Date().getFullYear()

    // Emil must be born:

    console.log(`Emil's birth year is: ${date - myArray[2]}`)

    
}

myFunnyLoop()