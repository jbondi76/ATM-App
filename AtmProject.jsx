const ATMDeposit = ({ onChange, isDeposit, isValid }) => {
  const choice = ['Deposit', 'Cash Back'];

  return (
    <label className="label huge">
      <h4>{choice[Number(!isDeposit)]}</h4>
      <input
        id="number-input"
        type="number"
        onChange={onChange}
        placeholder="Enter amount"
      />
      <input
        type="submit"
        disabled={!isValid}
        value="Submit"
        id="submit-input"
      />
    </label>
  );
};

const Account = () => {
  const [deposit, setDeposit] = React.useState(0);
  const [totalState, setTotalState] = React.useState(0);
  const [isDeposit, setIsDeposit] = React.useState(true);
  const [atmMode, setAtmMode] = React.useState('');
  const [validTransaction, setValidTransaction] = React.useState(false);

  const status = `Account Balance $ ${totalState}`;

  const handleChange = (event) => {
    const inputValue = Number(event.target.value);
  
    if (inputValue <= 0) {
      setValidTransaction(false);
      alert("Please enter a valid positive amount.");
    } else if (atmMode === 'Cash Back' && inputValue > totalState) {
      setValidTransaction(false);
      alert("Insufficient funds for cashback. Please enter a valid amount.");
    } else {
      setValidTransaction(true);
    }
  
    setDeposit(inputValue);
  };
  

  const handleSubmit = (event) => {
    const newTotal = isDeposit ? totalState + deposit : totalState - deposit;
    setTotalState(newTotal);
    setValidTransaction(false);
    event.preventDefault();
  };

  const handleModeSelect = (event) => {
    const selectedMode = event.target.value;
    setAtmMode(selectedMode);
    setValidTransaction(false);
    setIsDeposit(selectedMode === 'Deposit');
  };

  return (
    <form onSubmit={handleSubmit}>
      <>
        <h3 id="total">{status}</h3>
        <label htmlFor="mode-select">Select an action below to continue</label>
        <select
          onChange={(e) => handleModeSelect(e)}
          name="mode"
          id="mode-select"
        >
          <option value=""></option>
          <option value="Deposit">Deposit</option>
          <option value="Cash Back">Cash Back</option>
        </select>
        {atmMode && <ATMDeposit onChange={handleChange} isDeposit={isDeposit} isValid={validTransaction} />}
      </>
    </form>
  );
};

// ========================================
ReactDOM.render(<Account />, document.getElementById('root'));
