import {html} from "../../packages/arrow.js"

const registerForm = html`
    <form id="registerForm" action="/users/register" method="post">
        <div class="formGroup">
            <label for="username">Username</label>
            <input type="text" name="username" id="inputUsername" required/>
        </div>
        <div class="formGroup">
            <label for="email">Email</label>
            <input type="email" name="email" id="inputEmail" required>
        </div>
        <div class="formGroup">
            <label for="pasword">Password</label>
            <input type="password" name="password" id="inputPassword" required>
        </div>
        <div class="formGroup">
            <label for="verifypasword">Verify Password</label>
            <input type="password" name="verifypassword" id="inputVarifyPassword" required>
        </div>
        <div class="formGroup">
            <button class="formButton" type="submit">Send</button>
            <button class="formButton" type="reset">Clear</button>
        </div>
    </form>
`

export default registerForm;