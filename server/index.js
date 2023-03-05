const express = require('express');
const { PythonShell } = require('python-shell');

const app = express();
const port = 3000;

app.set('view engine', 'ejs');



app.get('/', (req, res) => {



    let program = {"type": "then", "arg1": {"type": "compair_filter", "arg1": {"type": "ticker", "ticker_name": "AMZN"}, "arg2": {"type": "moving_average", "arg1": {"type": "ticker", "ticker_name": "AMZN"}, "window": 30}, "direction": false}, "arg2": {"type": "compair_filter", "arg1": {"type": "ticker", "ticker_name": "GLD"}, "arg2": {"type": "moving_average", "arg1": {"type": "ticker", "ticker_name": "GLD"}, "window": 30}, "direction": false}}
        const { spawn } = require('child_process');

        // Spawn a child process
        // Spawn a child process in a different directory

        
        const child = spawn('python3.10', ['interpret.py', JSON.stringify(program)], { cwd: '../pyscripts' });

        // Listen for data from the child process

        

        child.stdout.on('data', (data) => {
            // output = `stdout: ${data}`;
            
            const values = {
                title: 'My Website',
                heading: 'Welcome to my website!',
                content: data
              };
            res.render('index', values);


        });

        // Listen for errors from the child process
        child.stderr.on('data', (data) => {
        console.error(`${data}`);
        });

        // Listen for the child process to exit
        child.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        });

       
        
    
    
});

app.get('/run-python', (req, res) => {
    // Specify the Python version
    
});



app.get('/chart', (req, res) => {



    let program = {"type": "then", "arg1": {"type": "compair_filter", "arg1": {"type": "ticker", "ticker_name": "AMZN"}, "arg2": {"type": "moving_average", "arg1": {"type": "ticker", "ticker_name": "AMZN"}, "window": 30}, "direction": false}, "arg2": {"type": "compair_filter", "arg1": {"type": "ticker", "ticker_name": "GLD"}, "arg2": {"type": "moving_average", "arg1": {"type": "ticker", "ticker_name": "GLD"}, "window": 30}, "direction": false}}
    const { spawn } = require('child_process');

        // Spawn a child process
        // Spawn a child process in a different directory

        
        const child = spawn('python3.10', ['interpret.py', JSON.stringify(program)], { cwd: '../pyscripts' });

        // Listen for data from the child process

        

       
        child.stdout.on('data', (data) => {
            const values = {
                title: 'My Website',
                heading: 'Welcome to my website!',
                content: data
              };

              intermed = JSON.parse(`${data}`)
            //   console.log(intermed)

            res.render('chart', { title: 'My Chart', data: JSON.stringify(intermed) });
            
        });

        // Listen for errors from the child process
        child.stderr.on('data', (data) => {
            console.error(`${data}`);
        });

        // Listen for the child process to exit
        child.on('close', (code) => {
        console.log(`child process exited with code ${code}`);

        // console.log(output)

        // obj = JSON.parse(output)
        // res.render('chart', { title: 'My Chart', data: JSON.stringify(data)});
        // res.render('chart', { title: 'My Chart', data: JSON.stringify(output).substring(0, JSON.stringify(output).length - 3)} );
        });













    
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});