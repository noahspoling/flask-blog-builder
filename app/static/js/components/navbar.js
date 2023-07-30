import {html} from "../packages/arrow.js"

const navbar = html`
    <nav>
        <a href="/">
            <h1 class="navTitle">ByteBlog</h1>
        </a>
        <ul class="navBarList">
            <li class="navBarItem">
                <a href="/Posts">
                    <h3 class="navBarItemText">
                        Posts
                    </h3>
                </a>
            </li>
            <li class="navBarItem">
                <a href="/Projects">
                    <h3 class="navBarItemText">
                        Projects
                    </h3>
                </a>
            </li>
            <li class="navBarItem">
                <a href="/AboutMe">
                    <h3 class="navBarItemText">
                        About Me
                    </h3>
                </a>
            </li>
            <li class="navBarItem">
                <a href="/ContactMe">
                    <h3 class="navBarItemText">
                        Contact Me
                    </h3>
                </a>
            </li>
        </ul>
        <ul>

        </ul>
    </nav>
`
export default navbar;