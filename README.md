<h1 align="center">lab_ctrl 🧑‍💻</h1>
<h4 align="center"> 
  A utility to administrate small/medium sized computer labs
</h4>

## Installation
lab_ctrl is a suit of softwares to achieve the end goal, Controlling your smal/medium sized computer labs.
Hence, this needs somewhat configurations and hardwares to do so. In that case, lab_ctrl v1.0.0 will need the following:
* A _parent_ computer: Can be \*nix/Windows
* Some _child_ computers _(can be one child also)_: v1.0.0 only supports Windows[10+ tested]

### Development Setup
* Father Setup **Dev**
  1. **Clone** the [repo](https://github.com/BirnadinErick/lab-ctrl.git) or Download the [zip](https://github.com/BirnadinErick/lab-ctrl/archive/refs/heads/master.zip)
  2. **installation work-in-progress**

* A Child Setup **Dev**
  1. **Clone** the [repo](https://github.com/BirnadinErick/lab-ctrl.git) or **Download** the [zip](https://github.com/BirnadinErick/lab-ctrl/archive/refs/heads/master.zip)
  2. **Move** the _child_ folder to a place you prefer
  3. _Recommended_ to use separate virtual envronment:- `python -m venv lab_ctrl_child_env__or__a_name_you_prefer`
  4. **Run** `pip install -r requirements.txt`(you also can use Pipfile)
  5. **Execute** `uvicorn api:api --reload`
  
Now you have a lab_ctrl setup in **dev-mode**

**For more info on terminology refer docs [terminology](Coming Soon⚠️)**

## Usage

## License
[MIT](LICENSE)
