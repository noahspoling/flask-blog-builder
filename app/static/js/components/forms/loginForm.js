import {html} from "../../packages/arrow.js"

const loginForm = html`
    <form>
        <div class="formGroup">
            <label for="Username">Username</label>
            <input type="text" name="Username" id="inputUsername" required/>
        </div>
        <div class="formGroup">
            <label for="Pasword">Email</label>
            <input type="password" name="Password" id="inputPassword" required>
        </div>
        <div class="formGroup">
            <button type="submit">Send</button>
            <button type="reset">Clear</button>
        </div>
    </form>
`

export default loginForm;