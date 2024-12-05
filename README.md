<h1>Speech to Text Generator</h1>

<h2>Description</h2>
<p>This Python application allows you to record your voice through the microphone and converts it into text using <strong>Google's Speech Recognition API</strong>. The recognized speech is saved to a text file (<code>you_said_this.txt</code>), with each entry timestamped. The program continuously listens for speech until the word <strong>"exit"</strong> is spoken, at which point it stops listening and saves all recognized text to the file.</p>

<h3>Key Features:</h3>
<ul>
    <li>Continuous speech recognition</li>
    <li>Saves recognized speech to a text file (<code>you_said_this.txt</code>)</li>
    <li>Timestamped entries for each recorded phrase</li>
    <li>Stops when the word <strong>"exit"</strong> is spoken</li>
</ul>

<h2>Requirements</h2>
<p>This project requires Python and the following dependencies:</p>
<ul>
    <li><strong>Python 3.x</strong> (preferably 3.6 or higher)</li>
    <li><strong>speech_recognition</strong> library</li>
    <li><strong>PyAudio</strong> for microphone input</li>
</ul>

<h3>Install Python</h3>
<p>Ensure that <strong>Python 3.x</strong> is installed on your system. You can download it from the official website: <a href="https://www.python.org/downloads/" target="_blank">Download Python</a></p>

<h2>Installation</h2>
<ol>
    <li><strong>Clone the repository</strong> to your local machine:
        <pre><code>git clone https://github.com/faisalrafiq031/speech-to-text-generator-using-python.git
cd speech-to-text-generator-using-python</code></pre>
    </li>
    <li><strong>Install required Python libraries</strong>:
        <pre><code>pip install SpeechRecognition
pip install PyAudio</code></pre>
    </li>
    <li>For Windows users, if <code>PyAudio</code> installation fails, use <code>pipwin</code> to install it:
        <pre><code>pip install pipwin
pipwin install pyaudio</code></pre>
    </li>
    <li><strong>Mac users</strong> might need to install <code>portaudio</code> using Homebrew:
        <pre><code>brew install portaudio</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<h3>Run the Script</h3>
<ol>
    <li>After setting up the project and installing the dependencies, run the <code>speech-to-text.py</code> script:
        <pre><code>python speech-to-text.py</code></pre>
    </li>
    <li>The program will start listening for your speech. When you speak, it will recognize and save the text in a file named <code>you_said_this.txt</code>.</li>
    <li>The program continues listening for speech until you say the word <strong>"exit"</strong>, at which point it will stop.</li>
</ol>

<h3>Output</h3>
<p>The text that you speak will be saved in a file called <code>you_said_this.txt</code> in the same directory as the script.</p>
<p>Each recognized phrase is timestamped for easy tracking.</p>

<h2>Example</h2>
<p>Here's an example interaction:</p>
<pre><code>Listening... Speak into the microphone (say 'exit' to stop).
You said: assistant manager
Listening... Speak into the microphone (say 'exit' to stop).
You said: hello beta hello
Listening... Speak into the microphone (say 'exit' to stop).
You said: exit
Exiting... Your speech has been saved.</code></pre>

<p>In the <code>you_said_this.txt</code> file, the entries would look something like this:</p>
<pre><code>[2024-12-02 14:25:30] assistant manager
[2024-12-02 14:25:40] hello beta hello
[2024-12-02 14:25:50] exit</code></pre>

<h2>Troubleshooting</h2>
<ul>
    <li><strong>Microphone not recognized:</strong> Make sure your microphone is working and properly connected.</li>
    <li><strong>Speech Recognition errors:</strong> If the recognition is poor, ensure you're speaking clearly and in a quiet environment. The Google API might have trouble with certain accents or background noise.</li>
    <li><strong>PyAudio installation issues (Windows users):</strong> Follow the instructions in the <a href="https://pypi.org/project/PyAudio/" target="_blank">PyAudio installation guide</a> or use <code>pipwin</code>.</li>
</ul>

<h2>Contributing</h2>
<p>Feel free to fork this project, contribute to the code, and submit issues. If you have suggestions or improvements, feel free to open a pull request!</p>

<h2>License</h2>
<p>This project is open source and available under the <a href="LICENSE" target="_blank">MIT License</a>.</p>
