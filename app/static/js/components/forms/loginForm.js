import {html} from "../../packages/arrow.js"

const loginForm = html`
    <form action="/users/login" method="post">
        <div class="formGroup">
            <label for="Username">Username</label>
            <input type="text" name="Username" id="inputUsername" required/>
        </div>
        <div class="formGroup">
            <label for="Pasword">Password</label>
            <input type="password" name="Password" id="inputPassword" required>
        </div>
        <div class="formGroup">
            <button class="formButton" type="submit">Send</button>
            <button class="formButton" type="reset">Clear</button>
        </div>
    </form>
`

export default loginForm;